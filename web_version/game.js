class Card {
    constructor(color, value) {
        this.color = color;
        this.value = value;
    }

    describe() {
        return `Card: ${this.color} ${this.value}`;
    }
}

class SpecialCard extends Card {
    constructor(color, value, type) {
        super(color, value);
        this.type = type;
    }

    describe() {
        return `SpecialCard: ${this.color} ${this.value}, Type: ${this.type}`;
    }
}

function MakeCards (){
	console.log("hi")
};

