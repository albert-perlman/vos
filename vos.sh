source .twilio
until python3 src/main/python/main.py; do
    echo "VOS crashed with exit code $?.  Respawning.." >&2
    sleep 1
done