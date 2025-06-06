function updateUniqueItems(itemsMap) {
    if (!(itemsMap instanceof Map)) {
	throw new Error('Cannot process');
    }

    for (const [key, value] of itemsMap.entries()) {
	if (value == 1) {
	    itemsMap.set(key, 100);
	}
    }
    return itemsMap;
}

export default updateUniqueItems;
