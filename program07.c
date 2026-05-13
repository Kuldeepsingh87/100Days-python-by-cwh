#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <semaphore.h>

#define BUFFER_SIZE 5


typedef struct {
    int buffer[BUFFER_SIZE];
    int in;
    int out;
    sem_t mutex;
    sem_t empty;
    sem_t full;
} shared_data;

int main() {
    int shmid;
    shared_data *data;


    shmid = shmget(IPC_PRIVATE, sizeof(shared_data), IPC_CREAT | 0666);
    data = (shared_data *)shmat(shmid, NULL, 0);


    data->in = 0;
    data->out = 0;

    sem_init(&data->mutex, 1, 1);
    sem_init(&data->empty, 1, BUFFER_SIZE);
    sem_init(&data->full, 1, 0);

    pid_t pid = fork();

    if (pid == 0) {
        
        for (int i = 0; i < 10; i++) {
            sem_wait(&data->full);
            sem_wait(&data->mutex);

            int item = data->buffer[data->out];
            printf("Consumed: %d\n", item);
            data->out = (data->out + 1) % BUFFER_SIZE;

            sem_post(&data->mutex);
            sem_post(&data->empty);

            sleep(1);
        }
    } else {
        
        for (int i = 0; i < 10; i++) {
            sem_wait(&data->empty);
            sem_wait(&data->mutex);

            data->buffer[data->in] = i;
            printf("Produced: %d\n", i);
            data->in = (data->in + 1) % BUFFER_SIZE;

            sem_post(&data->mutex);
            sem_post(&data->full);

            sleep(1);
        }

        wait(NULL);
    }


    sem_destroy(&data->mutex);
    sem_destroy(&data->empty);
    sem_destroy(&data->full);

    shmdt(data);
    shmctl(shmid, IPC_RMID, NULL);

    return 0;
}