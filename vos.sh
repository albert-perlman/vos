source .twilio
until fbs run; do
    echo "VOS crashed with exit code $?.  Respawning.." >&2
    sleep 1
done