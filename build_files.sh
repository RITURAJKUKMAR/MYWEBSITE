echo "======> INSTALLING REQUIREMENTS <======"
pip install -r requirements.txt
echo "======> REQUIREMENTS INSTALLED <======"

echo "======> COLLECTING STATIC FILES <======"
python3.13.1 manage.py colloctstatic --noinput --clear
echo "======> STATIC FILES COLLEDCTED <======"

echo "======> MAKE-MIGRATIONS <======"
python3.13.1 manage.py makemegrations --noinput
python3.13.1 manage.py migrate --noinput
echo "======> MAKE-MIGRATIONS-END <======"

