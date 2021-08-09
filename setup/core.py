

def size_predict(model, df):
    prediction = model.predict(df)[0]

    # Convert numerical prediction to categorical
    if prediction >= 6.50:
        pred = "XXXL"
    elif prediction >= 5.50:
        pred = "XXL"
    elif prediction >= 4.50:
        pred = "XL"
    elif prediction >= 3.50:
        pred = "L"
    elif prediction >= 2.50:
        pred = "M"
    elif prediction >= 1.8:
        pred = "S"
    elif prediction >= 1.20:
        pred = "XS"
    else:
        pred = "XXS"
    return pred