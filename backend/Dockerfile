# 1. Use an official Python runtime base image
FROM python:3.11-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Define the virtual environment folder path
#ENV VIRTUAL_ENV=/opt/venv

# 4. CRITICAL: "Activate" it by updating the environment PATH variable
#ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# 3. Copy requirements first to leverage Docker cache
COPY ./requirements.txt /

# 4. Install dependencies
RUN pip install --no-cache-dir -r /requirements.txt

#RUN python3 -m venv venv
#RUN venv/bin/activate
#RUN pip install --no-cache-dir --upgrade -r /requirements.txt

# 5. Copy the rest of the application code
COPY ./app .

# 6. Run the FastAPI application using Uvicorn
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
#CMD ["uvicorn", "main:app", "--reload"]
# FastAPI / Uvicorn example
#CMD ["sh", "-c", "sleep 20 && uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["sh", "-c", "sleep 20 && uvicorn main:app --host 0.0.0.0 --port 8000"]
#CMD ["sh", "-c", "tail -f /dev/null"]


#CMD ["python","--reload"]
