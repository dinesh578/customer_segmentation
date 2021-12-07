
import pandas as pd
 
data = pd.read_csv("\\prepared_data.csv")

def preprocess(d):
    from sklearn.preprocessing import StandardScaler
    # Removing (statistical) outliers for Amount
    Q1 = d.Amount.quantile(0.05)
    Q3 = d.Amount.quantile(0.95)
    IQR = Q3 - Q1
    d = d[(d.Amount >= Q1 - 1.5*IQR) & (d.Amount <= Q3 + 1.5*IQR)]

    # Removing (statistical) outliers for Recency
    Q1 = d.Recency.quantile(0.05)
    Q3 = d.Recency.quantile(0.95)
    IQR = Q3 - Q1
    d = d[(d.Recency >= Q1 - 1.5*IQR) & (d.Recency <= Q3 + 1.5*IQR)]
    # Removing (statistical) outliers for Frequency
    Q1 = d.Frequency.quantile(0.05)
    Q3 = d.Frequency.quantile(0.95)
    IQR = Q3 - Q1
    d = d[(d.Frequency >= Q1 - 1.5*IQR) & (d.Frequency <= Q3 + 1.5*IQR)]
    # Rescaling the attributes
    d = d[['Amount', 'Frequency', 'Recency']]
    # Instantiate
    scaler = StandardScaler()
    # fit_transform
    d= scaler.fit_transform(d)
    d.shape
    d = pd.DataFrame(d)
    d.columns = ['Amount', 'Frequency', 'Recency']
    return(d)
    

k=preprocess(data)
print(k)