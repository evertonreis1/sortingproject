function calcMinRun(n) {
	let r = 0;
	while (n >= 32) {
		r |= n & 1;
		n >>= 1;
	}
	return n + r;
}

function mergeSort(left, right) {
	let result = [];

	while (left.length !== 0 || right.length !== 0) {
		let leftItem = left[0];
		let rightItem = right[0];

		if (leftItem < rightItem || leftItem == rightItem) {
			result.push(leftItem);
			left.splice(0, 1);
		} else {
			result.push(rightItem);
			right.splice(0, 1);
		}
	}

	return result;
}

function insertionSort(arr) {
	let result = [];

	arr.forEach((current, currentIndex) => {
		let previousIndex = currentIndex - 1;
		let insertIn = result.length;

		while (current < result[previousIndex] && previousIndex >= 0) {
			insertIn = previousIndex;
			previousIndex--;
		}

		result.splice(insertIn, 0, current);
	});

	return result;
}

function timSort(arr) {
	let RUN = calcMinRun(arr.length);
	let runs = [];

	for (let index = 0; index < arr.length; index += RUN) {
		runs.push(arr.slice(index, index + RUN));
	}

	runs = runs.map((run) => insertionSort(run));

	while (runs.length > 1) {
		let left = runs[0];
		let right = runs[1];

		let merged = mergeSort(left, right);

		runs.splice(0, 2, merged);
	}

	return runs.flat();
}

console.log(timSort(arr));
