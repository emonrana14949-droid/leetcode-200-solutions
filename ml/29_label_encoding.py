# Label Encoding - turn class names into numbers.
from sklearn.preprocessing import LabelEncoder
def run():
    return LabelEncoder().fit_transform(["cat", "dog", "cat", "bird"])

if __name__ == "__main__":
    assert run().tolist() == [1, 2, 1, 0]
    print("ok")
