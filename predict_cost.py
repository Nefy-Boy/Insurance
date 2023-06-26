import joblib

def predict(data):
	lr = joblib.load('Insurance Model_new')
	return lr.predict(data)