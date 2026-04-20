class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        let countS = {}
        let countT = {}
        s.split("").sort().forEach(i => {
            countS[i]? countS[i]++ : countS[i] = 1 
        })
        t.split("").sort().forEach(i => {
            countT[i]? countT[i]++ : countT[i] = 1 
        })
        return JSON.stringify(countS) == JSON.stringify(countT)
    }
}
