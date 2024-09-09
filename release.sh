echo "[release.sh] Begin..."

echo "[release.sh] Tailwind:"
npm run tailwind-build

echo "[release.sh] Collect static"
python manage.py collectstatic --noinput

echo "[release.sh] End."

