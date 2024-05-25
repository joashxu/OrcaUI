import { readFileSync, mkdir, writeFileSync } from 'fs';
import { getIconData, matchIconName } from '@iconify/utils';

const TARGET = 'orcaui/templates/icons';
const CACHE = Object.create(null);


function loadIconSet(prefix) {
    let main = require.resolve(`@iconify-json/${prefix}/icons.json`);
    if (!main) {
        return;
    }

    if (CACHE[main]) {
        return CACHE[main];
    }

    try {
        const result = JSON.parse(readFileSync(main, 'utf8'));
        CACHE[main] = result;
        return result;
    }
    catch { }
}


function addDynamicIconSelectors(options) {
    const prefix = 'i';
    const outDir = `${TARGET}`;

    mkdir(outDir, { recursive: true }, (err) => { if (err) throw err; });

    return (({ matchComponents }) => {
        matchComponents({
            [prefix]: (icon) => {
                // Get icon identifier
                const nameParts = icon.split(/--|\:/);

                if (nameParts.length !== 2) { throw new Error(`Invalid icon name: "${icon}"`); }

                // Get icon set prefix and icon name
                const [iconSetPrefix, name] = nameParts;
                if (!(iconSetPrefix.match(matchIconName) && name.match(matchIconName))) {
                    throw new Error(`Invalid icon name: "${icon}"`);
                }

                // Load icon set
                const iconSet = loadIconSet(iconSetPrefix);
                if (!iconSet) {
                    throw new Error(
                        `Cannot load icon set for "${prefix}". Install "@iconify-json/${prefix}" as dev dependency?`
                    );
                }

                // Get icon data
                const data =  getIconData(iconSet, name);

                // Save data to file
                writeFileSync(`${__dirname}/${outDir}/${prefix}-[${icon}]`, data['body']);
                return;
           }
        });
    })
}

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './orcaui/templates/**/*.html',
      './orcaui/templates/**/*.yaml',
  ],
  plugins: [
      require('daisyui'),
      require('@iconify-json/heroicons'),
      addDynamicIconSelectors(),
  ],
  daisyui: {
      themes: ['light', 'dark'],
      styled: true,
  }
}
