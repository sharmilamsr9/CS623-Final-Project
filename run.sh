# migrations
chmod +x migrations.sh
./migrations.sh
echo "Migrations completed!"
# start server
cd ecommerce/
python manage.py runserver  0.0.0.0:8000