from diskplayerenum import State

class DiskPlayer:
    def __init__(self):
        self.state=State.EMPTY

    def insert_disk(self):
        if self.state == State.EMPTY:
            self.state = State.STOPPED
        else:
            raise ValueError("disk already inserted")
        
    def eject_disk(self):
        if self.state == State.EMPTY:
            raise ValueError("no disk inserted")
        else:
            self.state = State.EMPTY
    
    def play(self):
        if self.state in [State.PAUSED,State.STOPPED]:
            self.state = State.PLAYING

    def pause(self):
        if self.state == State.PLAYING:
            self.state = State.PAUSED
        else:
            raise ValueError("Can't pause when not playing")
        
    def stop(self):
        if self.state in [State.PLAYING,State.PAUSED]:
            self.state = State.STOPPED
        else:
            raise ValueError("can't stop when not playing or paused")

# disk_player.py
# ...

if __name__ == "__main__":
    actions = [
        DiskPlayer.insert_disk,
        DiskPlayer.play,
        DiskPlayer.pause,
        DiskPlayer.stop,
        DiskPlayer.eject_disk,
        DiskPlayer.insert_disk,
        DiskPlayer.play,
        DiskPlayer.stop,
        DiskPlayer.eject_disk,
    ]
    player = DiskPlayer()
    for action in actions:
        action(player)
        print(player.state)
