FROM python:3.8-buster

COPY . /poc-automation-testing

WORKDIR /poc-automation-testing

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x /poc-automation-testing/entrypoint.sh

ENTRYPOINT [ "/poc-automation-testing/entrypoint.sh" ]
CMD [ "api" ]