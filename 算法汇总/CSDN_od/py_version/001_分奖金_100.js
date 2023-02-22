/* JavaScript Node ACM模式 控制台输入获取 */
const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const lines = [];
rl.on("line", (line) => {
  lines.push(line);

  if (lines.length === 2) {
    const m = lines[0] - 0;
    const arr = lines[1].split(" ").map(Number);
    console.log(getResult(arr, m));
    lines.length = 0;
  }
});

function getResult(arr, m) {
  const ans = [];

  outter: for (let i = 0; i < m; i++) {
    for (let j = i + 1; j < m; j++) {
      if (arr[j] > arr[i]) {
        ans.push((j-i) * (arr[j] - arr[i])); // 距离 * 数字差值
        continue outter;
      }
    }
    ans.push(arr[i]);
  }

  return ans.join(" ");
}