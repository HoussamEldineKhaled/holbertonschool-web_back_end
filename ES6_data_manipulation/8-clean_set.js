function cleanSet(set, startString) {
    if (typeof startString !== 'string' || startString === '') {
	return '';
    }

    const filteredValue = [];

    for (const value of set) {
	if (typeof value === 'string' && value.startsWith(startString)) {
	    const remainingPart = value.slice(startString.length);
	    if (remainingPart !== '') {
		filteredValue.push(remainingPart);
	    }
	}
    }

    return filteredValue.join('-');
}

export default cleanSet;
