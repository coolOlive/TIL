// js로 큐를 구현해봤다.

class queue {
    constructor() {
        this.storage={}
        this.start=0
        this.end=0
    }
    
    size() {
        if(this.storage[this.end]===undefined) {
            return 0;
        } else {
            return this.end-this.start+1;
        }
    }
    
    add(value) {
        if (this.size()===0) {
            this.storage['0']=value
        } else {
            this.end+=1
            this.storage[this.end]=value
        }
    }
    
    popleft() {
        let tmp
        if(this.start==this.end) {
            tmp=this.storage[this.start]
            delete this.storage[this.start]
            this.start=0
            this.end=0
        } else {
            tmp=this.storage[this.start]
            delete this.storage[this.start]
            this.start+=1
        }
        return tmp
    }
    
    rotate(value) {
        this.add(value)
    }
    
    maxP() {
        return Math.max(...(Object.values(this.storage)))
    }
}

function solution(priorities, location) {
    const que = new queue()
    var ans=1
    
    priorities.forEach(v=>que.add(v))
    
    while (location>=0) {
        var tmp1=que.popleft()
        location-=1
        
        if (tmp1<que.maxP()) {
            if (location==-1) {
                location+=que.size()+1
            }
            que.rotate(tmp1)
        } else {
            if (location==-1) {
                break
            }
            ans+=1
        }
    }
    
    
    return ans;
}
