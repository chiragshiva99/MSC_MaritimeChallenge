

class MatchandLearn {
    constructor(totalTime, tiles) {
        this.tilesArray = tiles;
        this.totalTime = totalTime;
        this.timeRemaining = totalTime;
        this.timer = document.getElementById('time-remaining')
        this.ticker = document.getElementById('flips');
    }

    startGame() {
        this.totalClicks = 0;
        this.timeRemaining = this.totalTime;
        this.tileToCheck = null;
        this.matchedTiles = [];
        this.busy = true;
        setTimeout(() => {
            this.shuffleTiles(this.tilesArray);
            this.countdown = this.startCountdown();
            this.busy = false;
        }, 500)
        this.hideTiles();
        this.timer.innerText = this.timeRemaining;
        this.ticker.innerText = this.totalClicks;
    }
    startCountdown() {
        return setInterval(() => {
            this.timeRemaining--;
            this.timer.innerText = this.timeRemaining;
            if(this.timeRemaining === 0)
                this.gameOver();
        }, 500);
    }
    gameOver() {
        clearInterval(this.countdown);
        document.getElementById('game-over-text').classList.add('visible');
    }
    victory() {
        clearInterval(this.countdown);
        document.getElementById('winner-text').classList.add('visible');
    }
    hideTiles() {
        this.tilesArray.forEach(tile => {
            tile.classList.remove('visible');
            tile.classList.remove('matched');
        });
    }
    flipTile(tile) {
        if(this.canFlipTile(tile)) {
            this.totalClicks++;
            this.ticker.innerText = this.totalClicks;
            tile.classList.add('visible');

            if(this.tileToCheck) {
                this.checkForTileMatch(tile);
            } else {
                this.tileToCheck = tile;
            }
        }
    }
    checkForTileMatch(tile) {
        if(this.getTileType(tile) === this.getTileType(this.tileToCheck))
            this.tileMatch(tile, this.tileToCheck);
        else 
            this.tileMismatch(tile, this.tileToCheck);

        this.tileToCheck = null;
    }
    tileMatch(tile1, tile2) {
        this.matchedTiles.push(tile1);
        this.matchedTiles.push(tile2);
        tile1.classList.add('matched');
        tile2.classList.add('matched');
        if(this.matchedTiles.length === this.tilesArray.length)
            this.victory();
    }
    tileMismatch(tile1, tile2) {
        this.busy = true;
        setTimeout(() => {
            tile1.classList.remove('visible');
            tile2.classList.remove('visible');
            this.busy = false;
        }, 500);
    }
    shuffleTiles(tilesArray) { // Fisher-Yates Shuffle Algorithm.
        for (let i = tilesArray.length - 1; i > 0; i--) {
            let randIndex = Math.floor(Math.random() * (i + 1));
            tilesArray[randIndex].style.order = i;
            tilesArray[i].style.order = randIndex;
        }
    }
    getTileType(tile) {
        return tile.getElementsByClassName('tile-value')[0].src;
    }
    canFlipTile(tile) {
        return !this.busy && !this.matchedTiles.includes(tile) && tile !== this.tileToCheck;
    }
}

if (document.readyState == 'loading') {
    document.addEventListener('DOMContentLoaded', ready);
} else {
    ready();
}

function ready() {
    let overlays = Array.from(document.getElementsByClassName('overlay-text'));
    let tiles = Array.from(document.getElementsByClassName('tile'));
    let game = new MatchandLearn(100, tiles);

    overlays.forEach(overlay => {
        overlay.addEventListener('click', () => {
            overlay.classList.remove('visible');
            game.startGame();
        });
    });

    tiles.forEach(tile => {
        tile.addEventListener('click', () => {
            game.flipTile(tile);
        });
    });
}
