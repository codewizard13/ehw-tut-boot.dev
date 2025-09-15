/**
 * List Post Titles
 * Filename: list-post-title.js
 * Category: Tools
 * Date Created: 2024-12-11
 * 
 * Purpose: Generates list of markdown formatted links for any folder's 
 *  index page, listing all md posts in the folder.
 * 
 * Usage:
 * - node tools/list-post-titles.js --sourceDir "how-to"
 * - #GOTCHA: Ensure that you are referencing from the current folder in
 *   the bash terminal, NOT the current folder int VSCode Explorer sidebar.
 * - quotes may or may note be required around the sourceDir path
 * 
 * Sample Output:
 * 
 * References:
 * - 
 */
const fs = require('fs');
const path = require('path');
const { program } = require('commander');

program
    .option('-sd, --sourceDir <sourceDir>', 'Source Directory');

program.parse(process.argv);

const options = program.opts();

const start_dir = __dirname;
console.log(`start_dir: ${start_dir}`);

console.log(`options:`, options.sourceDir);

const folderPath = options.sourceDir ? options.sourceDir : start_dir;

try {
    
    // Define files
    const files = fs.readdirSync(folderPath);
    console.log('Files:', files);

    console.log(`////////// POST TITLES ///////////\n`)

    files.forEach(file => {
        const filePath = path.join(folderPath, file);
        const data = fs.readFileSync(filePath, 'utf8');

        const regex = /^# (.*)/m;
        const match = data.match(regex);

        if (match) {
            const post_title = match[1];
            console.log(`- [${post_title}](${file})`);
            // console.log(post_title);
        }
    });

} catch (error) {
    console.error(`Error reading directory: ${folderPath}`, error);
}


