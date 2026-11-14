from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_linked_list(values: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> list:
    res = list()
    while head:
        res.append(head.val)
        head = head.next
    return res


class Solution:
    # 1. Поиск двух слагаемых (Two Sum)
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return list()

    # 2. Сложение чисел в односвязных списках (Add Two Numbers)
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10
            cur.next = ListNode(total % 10)

            cur = cur.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next

    # 3. Слияние двух отсортированных списков (Merge Two Sorted Lists)
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        cur = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 else list2
        return dummy.next

    # 4. Комбинации с заданной суммой (Combination Sum)
    def combinationSum(self, candidates: list, target: int) -> list:
        res = list()

        def backtrack(start: int, current: list, total: int):
            if total == target:
                res.append(list(current))
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                current.append(candidates[i])
                backtrack(i, current, total + candidates[i])
                current.pop()

        backtrack(0, list(), 0)
        return res

    # 5. Бинарный поиск (Binary Search)
    def search(self, nums: list, target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    # 6. Проверка корректности скобок (Valid Parentheses)
    def isValid(self, s: str) -> bool:
        stack = list()
        pairs = {')': '(', ']': '[', '}': '{'}

        for char in s:
            if char in pairs:
                if not stack or stack.pop() != pairs[char]:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0

    # 7. Максимальная прибыль от одной сделки (Best Time to Buy and Sell Stock)
    def maxProfit(self, prices: list) -> int:
        zero = 0
        min_price = prices[zero]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit

    # 8. Разворот односвязного списка (Reverse Linked List)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev

    # 9. Объединение пересекающихся интервалов (Merge Intervals)
    def merge(self, intervals: list) -> list:
        zero = 0
        one = 1
        last = -1
        intervals.sort(key=lambda x: x[zero])
        merged = [intervals[zero]]

        for start, end in intervals[one:]:
            last_end = merged[last][one]
            if start <= last_end:
                merged[last][one] = max(last_end, end)
            else:
                merged.append([start, end])

        return merged

    # 10. Количество островов в матрице (Number of Islands)
    def numIslands(self, grid: list) -> int:
        if not grid:
            return 0
        zero = 0
        rows, cols = len(grid), len(grid[zero])
        islands = 0

        def dfs(r: int, c: int):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r, c)

        return islands

    # 11. Минимальное число монет для заданной суммы (Coin Change)
    def coinChange(self, coins: list, amount: int) -> int:
        zero = 0
        dp = [amount + 1] * (amount + 1)
        dp[zero] = 0

        for a in range(1, amount + 1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


def main():
    sol = Solution()
    print("=== ЛАБОРАТОРНАЯ РАБОТА ПО АЛГОРИТМАМ И СТРУКТУРАМ ДАННЫХ ===\n")

    # 1
    nums1, target1 = list((2, 7, 11, 15)), 9
    print(f"1. Two Sum | Вход: nums={nums1}, target={target1} -> Ответ: {sol.twoSum(nums1, target1)}")

    # 2
    raw_l1, raw_l2 = list((2, 4, 3)), list((5, 6, 4))
    res2 = linked_list_to_list(sol.addTwoNumbers(build_linked_list(raw_l1), build_linked_list(raw_l2)))
    print(f"2. Add Two Numbers | Вход: l1={raw_l1}, l2={raw_l2} -> Ответ: {res2}")

    # 3
    raw_list1, raw_list2 = list((1, 2, 4)), list((1, 3, 4))
    res3 = linked_list_to_list(sol.mergeTwoLists(build_linked_list(raw_list1), build_linked_list(raw_list2)))
    print(f"3. Merge Two Sorted Lists | Вход: list1={raw_list1}, list2={raw_list2} -> Ответ: {res3}")

    # 4
    cand4, target4 = list((2, 3, 6, 7)), 7
    print(f"4. Combination Sum | Вход: candidates={cand4}, target={target4} -> Ответ: {sol.combinationSum(cand4, target4)}")

    # 5
    nums5, target5 = list((-1, 0, 3, 5, 9, 12)), 9
    print(f"5. Binary Search | Вход: nums={nums5}, target={target5} -> Ответ: {sol.search(nums5, target5)}")

    # 6
    s6 = "()[]{}"
    print(f"6. Valid Parentheses | Вход: s='{s6}' -> Ответ: {sol.isValid(s6)}")

    # 7
    prices7 = list((7, 1, 5, 3, 6, 4))
    print(f"7. Max Profit | Вход: prices={prices7} -> Ответ: {sol.maxProfit(prices7)}")

    # 8
    raw_head8 = list((1, 2, 3, 4, 5))
    res8 = linked_list_to_list(sol.reverseList(build_linked_list(raw_head8)))
    print(f"8. Reverse Linked List | Вход: head={raw_head8} -> Ответ: {res8}")

    # 9
    intervals9 = [list((1, 3)), list((2, 6)), list((8, 10)), list((15, 18))]
    print(f"9. Merge Intervals | Вход: intervals={intervals9} -> Ответ: {sol.merge(intervals9)}")

    # 10
    grid10 = [
        list(("1", "1", "0", "0", "0")),
        list(("1", "1", "0", "0", "0")),
        list(("0", "0", "1", "0", "0")),
        list(("0", "0", "0", "1", "1"))
    ]
    print(f"10. Number of Islands | Вход: матрица 4x5 -> Ответ: {sol.numIslands(grid10)}")

    # 11
    coins11, amount11 = list((1, 2, 5)), 11
    print(f"11. Coin Change | Вход: coins={coins11}, amount={amount11} -> Ответ: {sol.coinChange(coins11, amount11)}")


if __name__ == "__main__":
    main()
