FROM python:3.10

ARG APP_ROOT="/var/lib/severstal_tt"

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:${APP_ROOT}"

ENV APP_USER service_user
ENV C_FORCE_ROOT true

RUN groupadd -r docker \
    && useradd -r -m \
    --home-dir ${APP_ROOT} \
    -s /usr/sbin/nologin \
    -g docker ${APP_USER}
RUN usermod -aG sudo ${APP_USER}

WORKDIR ${APP_ROOT}

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD ["python3", "main.py"]

