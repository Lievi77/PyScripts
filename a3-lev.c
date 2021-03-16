
/*

Lev Cesar Guzman Aparicio - 300038033

Assignment 3: Semaphores,MUTEX

*/

#include<stdio.h> //std i/o 
#include<string.h> //string library
#include<pthread.h> //threads
#include<stdlib.h> //std lib
#include<unistd.h> //unis std lib
#include <semaphore.h>  //semaphores


/*
Problem Premise:
TA office hours:
    - office is small
    - only one desk with computer to help students
    - waiting room has 3 chars for students to wait their turn 
    - If no students are waiting for help, the TA takes a nap (sleeps)
    - If a student encounters the TA busy, he or she sits in the waiting chairs.
    -If no chairs are available, the student leaves and will come back at a later time

    Solution uses: POSIX threads, mutex locks, semaphores.

    Solution coordinates the activities of the TA and Students.


    Details:
    1. Using Pthredas, create n (threads) students
    2. Use a thread for the TA.
    3. Students alternate between programming and requesting for help
    4. If TA is available, they will receive help
    5. Otherwise they will sit in one of the (3) waiting chairs.
    6. If no chairs are available, then the student will resume programming.
    7. If a student arrives and the TA is asleep, the TA will be notified via a semaphore.
    8. When the TA finishes helping a student, the TA will check if there are students awaiting.
    9. If no students are awaiting help, the TA will enter sleep mode
*/

pthread_t ta; //var to hold the TA Thread
pthread_mutex_t lock; //var to hold the mutex 
sem_t semaphore; //semaphore
pthread_t waiting_queue; //use buffer


void* student(void* args){


    return NULL;
}

void* teaching_assistant(void* args){


    return NULL;
}


/* Main method */
int main(int argc, char const *argv[]){
    
    int n_students;

    if( argc == 2 && sscanf( argv[1],"%d"  ,&n_students) == 1 ){

        if(n_students < 1){

            printf("Number of students must at least be 1 (%d)\n", n_students);
        }else{

            //we have correct arguments from here on 
            if(pthread_mutex_init(&lock, NULL) != 0 ){ //i.e, an error was raised
                fprintf(stderr,"Error in mutex creation\n");
            }


            int ta_id = -1; //TA THREAD
            sem_init(&semaphore,0,0); //init semaphore to value of 0 i.e, sleeping
            pthread_create(&ta, NULL, &thread, &ta_id);
            pthread_join(ta, NULL );

            /*pthread_t thread_id[n_students]; // n student threads
            for (int i = 0; i < n_students; i++){ //creates n student threads
                //printf("%d", i);
                pthread_create(&thread_id[i], NULL, &student , &i); //the i will uniquely identify each student
                pthread_join(thread_id[i], NULL);
            }*/

            pthread_mutex_destroy(&lock); //good practice to destroy mutex when done
            sem_destroy(&semaphore);
        }

    }else{
        fprintf(stderr, "Incorrect arguments\n");
    }
    return 0;
}