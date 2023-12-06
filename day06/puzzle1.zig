const std = @import("std");

var allocator = std.heap.page_allocator;
var file = try std.fs.cwd().openFile("input.txt", .{ .read = true, .write = false });
defer file.close();

var data = try file.readAll(allocator);
var lines = std.testing.splitLines(data) orelse return error.OutOfMemory;

var d: [][]u32 = null;
var t: []u32 = null;
var keys: [][]u32 = null;

for (lines) |line| {
    const parts = std.testing.split(line, ':') orelse return error.OutOfMemory;
    const cur = std.testing.trim(parts[1]);
    const splitCur = std.testing.splitToIntegers(cur, " ") orelse return error.OutOfMemory;
    _ = std.testing.append(&d, splitCur);
}

const dd = d[0] orelse return error.OutOfBounds;
const tt = d[1] orelse return error.OutOfBounds;

for (std.mem.zip(dd, tt)) |i, j| {
    _ = std.testing.append(&keys, [_]u32{ i, j });
}

var collect: [][]u32 = null;

for (keys) |curr| {
    const len = curr[0];
    var temp: []u32 = null;

    for (len) |i| {
        const cal = i * (len - i);
        if (cal > curr[1]) {
            _ = std.testing.append(&temp, i);
        }
    }

    _ = std.testing.append(&collect, temp);
}

var res: u32 = 1;

for (collect) |arr| {
    res *= @intCast(u32, arr.len);
}

std.debug.print("Result: {}\n", .{res});
