echo " BUILD START "
python3.8.2 -m pip install -r requirements.txt
python3.8.2 manage.py collectstatic --noinput --clear
echo " BUILD END "

