#!/bin/bash

PORT=8501
PID=$(lsof -t -i:$PORT)

if [ -z "$PID" ]; then
  echo "No process found running on port $PORT"
else
  echo "Killing process $PID running on port $PORT"
  kill -9 "$PID"
  echo "Process killed."
fi
nohup streamlit run app.py --server.port 8501  --server.address 0.0.0.0 &
