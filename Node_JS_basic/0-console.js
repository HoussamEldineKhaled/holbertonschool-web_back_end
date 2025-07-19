/**
 *  Display STDOUT message.
 * @param {String} message 
 */
function displayMessage(message){
    process.stdout.write(message)
}

module.exports = displayMessage;
