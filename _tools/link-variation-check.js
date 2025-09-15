/**
 * Link Variation Checker
 * Filename: link-variation-check.js
 * Category: Tools
 * Date Created: 2024-12-13
 * Created By: Eric Hepperle
 * 
 * Purpose: Tests all versions of a link including http, https, and www.
 * 
 * Usage:
 * - node tools/link-variation-checks.js --domain example.com
 * 
 * Sample Output:
 * 
 * domain: elijahstreams.com
 * ┌─────────┬────────────────┐
 * │ (index) │ Values         │
 * ├─────────┼────────────────┤
 * │ 0       │ 'http://'      │
 * │ 1       │ 'https://'     │
 * │ 2       │ 'http://www.'  │
 * │ 3       │ 'https://www.' │
 * └─────────┴────────────────┘
 * ////////// URL VARIATIONS ///////////
 * 
 * DOMAIN: elijahstreams.com
 * 
 * Variation [http://]:  <a href="http://elijahstreams.com" target="_blank">http://elijahstreams.com</a>   
 * Variation [https://]:  <a href="https://elijahstreams.com" target="_blank">https://elijahstreams.com</a>
 * Variation [http://www.]:  <a href="http://www.elijahstreams.com" target="_blank">http://www.elijahstream
 * s.com</a>
 * Variation [https://www.]:  <a href="https://www.elijahstreams.com" target="_blank">https://www.elijahstr
 * eams.com</a>
 * 
 * //////////// DONATE VARIATIONS
 * 
 * http://elijahstreams.com/Donate
 * https://elijahstreams.com/Donate
 * http://www.elijahstreams.com/Donate
 * https://www.elijahstreams.com/Donate
 * 
 * References:
 * - 
 */
// const fs = require('fs');
// const path = require('path');
const { program } = require('commander');

const today = new Date()
const thisMonthNum = today.getMonth() + 1;
console.log("thisMonthNum", thisMonthNum);
const thisYear2dig = today.getFullYear() % 100;
console.log(`thisYear2dig: ${thisYear2dig}`)


const monthName = today.toLocaleString('default', { month: 'long' }); // 'December'
console.log(monthName); 

// Get parse command line args with commander
program
    .option('-url, --domain <domain>', 'URL Domain');

program.parse(process.argv);
const options = program.opts();

// Define url base as domain
const domain = options.domain ? options.domain : 'google.com'
console.log(`domain: ${domain}`);

// Define array of variations
const variations = [
    'http://', 'https://', 'http://www.', 'https://www.'
]
console.table(variations)

donate_vars = ''
month_donate_vars = ''

try {

    console.log(`////////// URL VARIATIONS ///////////\n`)
    console.log(`DOMAIN:\t${domain}\n`)

    variations.forEach(variation => {
        const fullUrl = variation + domain

        const anchor = `<a href="${fullUrl}" target="_blank">${fullUrl}</a>`

        // console.log(`Variation [${variation}]:  ${fullUrl}`)
        // console.log(`Variation [${variation}]:  ${anchor}`)
        console.log(`Variation [${variation}]:  ${anchor}`)

        // Create 'Donate' variations
        donate_vars += `${fullUrl}/Donate\n`


    });

    console.log(`\n//////////// DONATE VARIATIONS\n`)
    console.log(donate_vars)

} catch (error) {
    console.error(`Error reading directory: ${folderPath}`, error);
}


