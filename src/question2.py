class Orders:
    def _validate_inputs(self, requests: list[int], n_max: int) -> None:
        """
        Validates the inputs for a list of requests and a maximum value.

        Args:
            requests (list[int]): List of request integers.
            n_max (int): Maximum value.

        Raises:
            Exception: If the list of requests is empty or None.
            Exception: If the maximum value is invalid (None or less than or equal to 0).
        """
        if requests is None or len(requests) <= 0:
            raise Exception("Não há requisições abertas.")
        
        if n_max is None or n_max <= 0:
            raise Exception("Quantidade de valor máximo inválido.")


    def combine_orders(self, requests, n_max):
        trips = []
        index_requests_used = set()

        self._validate_inputs(requests, n_max)

        for i, request_i in enumerate(requests):
            if i in index_requests_used:
                continue

            best_combination = None

            for j, request_j in enumerate(requests[i + 1:], start=i + 1):
                if j in index_requests_used:
                    continue

                sum_actual = request_i + request_j
                if sum_actual <= n_max:
                    if best_combination is None or requests[best_combination['I']] + requests[best_combination['J']] < sum_actual:
                        best_combination = {'I': i, 'J': j}

            if best_combination is None:
                trips.append(i)
                index_requests_used.add(i)
            else:
                index_requests_used.add(best_combination['I'])
                index_requests_used.add(best_combination['J'])
                trips.append(best_combination)

        return len(trips)
