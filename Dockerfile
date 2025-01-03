FROM python:3.12.0

# устанавливаем переменные окружения
ENV HOME=/home/vbif \
    APP_HOME=/home/vbif/app \
    PYTHONPATH="$PYTHONPATH:/home/vbif" \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# создаем домашнюю директорию для пользователя(/home/fast) и директорию для проекта(/home/fast/app)
# создаем группу fast
# создаем отдельного пользователя fast
RUN mkdir -p $APP_HOME \
 && groupadd -r vbif\
 && useradd -r -g vbif vbif

# устанавливаем рабочую директорию
WORKDIR $HOME

COPY poetry.lock pyproject.toml ./

# обновление pip
# установка зависимостей из списка requirements.txt
# изменение владельца, для всех директорий и файлов проекта, на пользователя fast

RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

# копирование проекта FastAPI в рабочую директорию
COPY . $APP_HOME

# изменение рабочего пользователя на fast
USER vbif