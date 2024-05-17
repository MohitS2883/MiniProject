def returnSuggestions(terrain):
    sunsug = [
        'Stay hydrated to prevent dehydration in sandy environments',
        'Protect yourself from the sun with sunscreen and appropriate clothing',
        'Watch for sand hazards like hidden holes or quicksand',
        'Be cautious of wildlife such as snakes or insects in sandy areas',
        'Dress in lightweight, breathable clothing to stay comfortable and protect against sun exposure and sand irritation'
    ]
    rockysug = [
        'Wear sturdy footwear for stability on rocky terrain',
        'Use caution when climbing to test handholds and watch for loose rocks',
        'Stick to marked trails to avoid hazardous or unstable areas',
        'Be prepared for changes in elevation and steep terrain',
        'Bring essential gear like water, first aid kit, and weather-appropriate clothing for rocky conditions'
    ]
    marshysug = [
        'Wear waterproof footwear to navigate soggy terrain',
        'Use caution to avoid sinking in soft or unstable ground',
        'Stay on designated trails to protect fragile marsh ecosystems',
        'Be aware of wildlife such as snakes and insects commonly found in marshes',
        'Bring insect repellent, extra clothing, and water to stay comfortable and safe in marshy environments'
    ]
    grassysug = [
        'Dress in lightweight, protective clothing to shield against sun, insects, and scratches',
        'Watch for uneven terrain and hidden obstacles when walking in grassy areas',
        'Stay alert for wildlife like snakes or rodents, and keep a safe distance to avoid confrontation',
        'Bring a lightweight rain jacket or poncho for unexpected weather changes'
    ]
    dic = {
        'Sandy':sunsug,
        'Rocky':rockysug,
        'Marshy':marshysug,
        'Grassy':grassysug
    }
    return dic[terrain]