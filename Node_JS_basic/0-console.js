/**
 *  Display STDOUT message.
 * @param {String} message 
 */
const displayMessage = (message) => {
    process.stdout.write(message)
}

module.exports = displayMessage;
