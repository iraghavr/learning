from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)

        units = 0
        queue = deque()
        in_queue = set()

        while counter:
            if len(queue) == n + 1:
                to_remove = queue.popleft()
                if to_remove:
                    in_queue.remove(to_remove)

            for task, count in sorted(counter.items(), key=lambda x: (-x[1])):
                if task in in_queue:
                    continue

                queue.append(task)
                in_queue.add(task)
                units += 1

                counter[task] -= 1

                if counter[task] == 0:
                    counter.pop(task)

                break
            else:
                queue.append(None)
                units += 1

        while queue and queue[-1] is None:
            queue.pop()
            units -= 1

        return units
