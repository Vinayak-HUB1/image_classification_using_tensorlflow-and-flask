<!-- create environment -->
conda create --prefix ./env python=3.6 -y


<!-- install requirements file -->
pip install -r requirements.txt


<!-- run app file -->
python app.py



<!-- for training the cnn model in local -->
1.unzip the image_folder [cats_and_dogs_filtered.zip]
2.run cnn.py file
