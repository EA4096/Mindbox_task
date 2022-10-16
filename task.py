import numpy as np


def func1(n_customers, all_clients=np.arange(10000, 10000000)):  # ID клиентов, состоящие из 5-7 цифр

    if n_customers > all_clients[-1]:
        return 'Указанных ID нет в базе'

    needed_clients = all_clients[:n_customers]
    groups = np.zeros(n_customers)

    k = len(list(str(n_customers)))

    for i in range(k):
        groups = groups + needed_clients % 10
        needed_clients = needed_clients // 10

    return np.asarray((np.unique(groups, return_counts=True)), dtype=int).T


def func2(n_customers, n_first_id, all_clients=np.arange(10000, 10000000)):
    n_last_id = n_first_id + n_customers

    if (n_first_id < all_clients[0]) | (n_last_id > all_clients[-1]):
        return 'Указанных ID нет в базе'

    # Если под "первый ID в последовательности" понимается номер его позиции в последовательности
    needed_clients = all_clients[n_first_id:n_last_id]

    # Если само значение ID: [np.where(all_clients == n_first_id)][:n_customers]

    groups = np.zeros(n_customers)

    k = len(list(str(n_last_id)))

    for i in range(k):
        groups = groups + needed_clients % 10
        needed_clients = needed_clients // 10

    return np.asarray((np.unique(groups, return_counts=True)), dtype=int).T
