FROM python:3.9.10

WORKDIR /usr/src/handle_data

COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "handle_data.py" ]
