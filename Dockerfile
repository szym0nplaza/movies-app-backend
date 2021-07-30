FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install -r requirements.txt
RUN python manage.py migrate
COPY . /backend/
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]