class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
       s = s.split("").toSorted()
       t = t.split("").toSorted()
       return s.length == t.length && s.every((val, index) => val == t[index])
    }
}
