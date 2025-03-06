FROM python:3.12

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user
ARG SRC=z1.c

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} && \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY --chown=${USER}:555 ./docker/service/entrypoint.sh ./entrypoint.sh
COPY --chown=${USER}:555 ./docker/service/start.sh ./start.sh

RUN chmod +x ./entrypoint.sh ./start.sh

COPY --chown=${USER}:555 ./Makefile Makefile
COPY --chown=${USER}:555 ./bin bin
COPY --chown=${USER}:555 ./cases cases
COPY --chown=${USER}:555 ./main.py main.py

COPY --chown=${USER}:555 ./${SRC} /z1.c

ENTRYPOINT ["./entrypoint.sh"]
CMD ["./start.sh"]
