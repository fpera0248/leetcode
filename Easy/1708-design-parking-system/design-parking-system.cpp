class ParkingSystem {
public:
    map<int,int> spots;
    ParkingSystem(int big, int medium, int small) {
        spots[1] = big;
        spots[2] = medium;
        spots[3] = small;
    }
    
    bool addCar(int carType) {
        if(spots[carType]<=0) return false;
        spots[carType]--;
        return true;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */