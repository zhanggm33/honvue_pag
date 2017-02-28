pid_file="logs/uwsgi.pid"
PID=$(cat ${pid_file})
echo $PID
kill -9 ${PID}
echo "uwSGI stop done!"
