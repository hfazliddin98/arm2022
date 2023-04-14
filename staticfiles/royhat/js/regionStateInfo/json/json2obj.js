const fs = require('fs');

  // Read data from the JSON files
  const districts = JSON.parse(fs.readFileSync('./districts.json'));
  const regions = JSON.parse(fs.readFileSync('./regions.json'));
  const villages = JSON.parse(fs.readFileSync('./villages.json'));

  // Create an object to hold the converted data
  const countryStateInfo = {};

  // Loop through the regions and create a nested object for each one
  regions.forEach(region => {
    countryStateInfo[region.name_uz] = {};

    // Loop through the districts that belong to the current region
    const regionDistricts = districts.filter(district => district.region_id === region.id);
    regionDistricts.forEach(district => {
      countryStateInfo[region.name_uz][district.name_uz] = [];

      // Loop through the villages that belong to the current district
      const districtVillages = villages.filter(village => village.district_id === district.id);
      districtVillages.forEach(village => {
        countryStateInfo[region.name_uz][district.name_uz].push(village.name_uz);
      });
    });
  });

  fs.writeFileSync('./result.txt', JSON.stringify(countryStateInfo, null, 2), (err)=> {
    if(err) console.log(err)
  })

  // Output the final object
  console.log(countryStateInfo);

////////////////////////////////////////////////////////////
