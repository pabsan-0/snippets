TARGET=main
CC=g++
OBJS=main.o
SRCS=main.c

${TARGET}: ${OBJS}
	${CC} -o ${TARGET} ${OBJS}

clean:
	rm -rf *.o ${TARGET}

main.o: main.c
