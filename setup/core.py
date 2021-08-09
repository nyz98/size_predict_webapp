

def size_predict(model, df):
    prediction = model.predict(df)[0]

    # Convert numerical prediction to categorical
    if prediction >= 6.50:
        pred = "XXXL"
    elif prediction >= 6.00:
        pred = "XXL"
    elif prediction >= 5.30:
        pred = "XL"
    elif prediction >= 4.10:
        pred = "L"
    elif prediction >= 3.40:
        pred = "M"
    elif prediction >= 2.70:
        pred = "S"
    elif prediction >= 2.00:
        pred = "XS"
    else:
        pred = "XXS"
    return pred