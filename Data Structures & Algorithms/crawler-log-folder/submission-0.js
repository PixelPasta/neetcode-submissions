class Solution {
    /**
     * @param {string[]} logs
     * @return {number}
     */
    minOperations(logs) {
        let stack = []
        for (let i=0; i < logs.length;i++) {
            if (logs[i] == './') {
                continue
            }
            else if (logs[i] == '../') {
                stack.pop()
            }
            else {
                stack.push(logs[i])
            }
        }
        return stack.length
    }
}
