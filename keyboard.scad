include <keys.scad>

for (i = [0:len(keys) - 1]) {
    x = keys[i][0];
    y = keys[i][1];
    rot = keys[i][2];
    translate([x, y, 0]) {
        rotate([0, 0, rot]) {
            cube([18, 18, 5], center=true);
        }
    }
}