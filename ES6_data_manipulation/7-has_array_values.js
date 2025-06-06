function hasValuesFromArray(sett, arrray) {
    return arrray.every(element => sett.has(element));
}

export default hasValuesFromArray;
