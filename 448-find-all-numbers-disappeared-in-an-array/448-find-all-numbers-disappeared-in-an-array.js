/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(arr) {
      const set = new Set(arr);

      const allNums = []
      for (let i = 1; i <= arr.length; ++i) {
        allNums.push(i);
      }

      const res = []
      allNums.forEach(num => {
        if (!set.has(num)) res.push(num);
      })

      return res;
};