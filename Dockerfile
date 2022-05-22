FROM node:16

WORKDIR /app
ENV projectName "frontend"
COPY ./${projectName}/package.json .
COPY ./${projectName} .
# replace the next 3 lines if you use a different frontend framework
RUN npm i -g @quasar/cli
RUN npm i
RUN quasar build


FROM python:3.10-buster

WORKDIR /app
COPY / .
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY --from=0 /app/dist/ dist
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]