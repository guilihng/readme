import matplotlib.pyplot as plt
import tensorflow as tf
boston_housing =tf.keras.datasets.boston_housing
(train_x, train_y), (_, _) = boston_housing.load_data(test_split=0)
plt.rcParams['font.sans-serif'] = "SimHei"
plt.rcParams['axes.unicode_minus'] = False
titles = ["CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
          "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"]
aa = plt.figure('aa', figsize=(9, 9))
for i in range(13):
    plt.subplot(4, 4, (i + 1))
    plt.scatter(train_x[:, i], train_y)
    plt.xlabel(titles[i])
    plt.ylabel("Price($1000's)")
    plt.title(str(i + 1) + "." + titles[i] + " - Price")

plt.tight_layout(rect=[0, 0, 1, 0.9])
plt.suptitle("各个属性与房价的关系", fontsize=20)
plt.show()

bb = plt.figure('aa')
for x in range(13):
    print(x + 1, titles[x], sep="--")

m = int(input("请选择属性:"))
plt.subplot()
plt.scatter(train_x[:, m - 1], train_y)
plt.xlabel(titles[m - 1])
plt.ylabel("Price($1000's)")
plt.title(str(m) + "." + titles[m - 1] + " - Price")
plt.show()
